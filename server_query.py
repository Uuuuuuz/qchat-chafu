import a2s
from flask import Flask, request, jsonify

app = Flask(__name__)

def query_server(server_ip_with_port):
    if ":" in server_ip_with_port:
        server_ip, port = server_ip_with_port.split(":")
        port = int(port)
    else:
        server_ip = server_ip_with_port
        port = 27015  # 默认端口

    server_address = (server_ip, port)
    try:
        print(f"Querying server: {server_address}")
        info = a2s.info(server_address, timeout=30)

        players = a2s.players(server_address, timeout=10)

        print("Server info:", info)
        print("Players:", players)

        response = {
            "server_name": info.server_name,
            "map": info.map_name,
            "players": f"{info.player_count} / {info.max_players}",
            "player_list": [player.name for player in players]
        }
        return response
    except Exception as e:
        print(f"Error in query_server: {e}")
        return {"error": str(e)}

@app.route('/query_server', methods=['POST'])
def handle_query():
    data = request.json
    print("Received data:", data)
    message = data.get('message', '')

    if message.startswith("查询服务器"):
        try:
            server_ip_with_port = message.split(" ")[1]
            result = query_server(server_ip_with_port)
            if "error" in result:
                return jsonify({"reply": f"查询失败: {result['error']}"})
            else:
                return jsonify({
                    "reply": f"服务器: {result['server_name']}\n地图: {result['map']}\n玩家数: {result['players']}\n玩家列表: {', '.join(result['player_list'])}"
                })
        except Exception as e:
            return jsonify({"reply": f"查询失败: {e}"})
    else:
        return jsonify({"reply": "指令格式不正确，请使用：查询服务器 <服务器IP>"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
