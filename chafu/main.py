from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import httpx
import re
import logging


@register(name="ServerQueryPlugin", description="查询服务器插件", version="0.1", author="zzseki")
class ServerQueryPlugin(BasePlugin):
    
    def __init__(self, host: APIHost):
        self.logger = logging.getLogger(__name__)

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        receive_text = ctx.event.text_message
        QUERY_PATTERN = re.compile(r"查服：(.+)")
        match = QUERY_PATTERN.search(receive_text)
        if match:
            server_ip_with_port = match.group(1)
            result = await self.query_server(server_ip_with_port)
            ctx.add_return("reply", [result])
            ctx.prevent_default()

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        receive_text = ctx.event.text_message
        QUERY_PATTERN = re.compile(r"查服：(.+)")
        match = QUERY_PATTERN.search(receive_text)
        if match:
            server_ip_with_port = match.group(1)
            result = await self.query_server(server_ip_with_port)
            ctx.add_return("reply", [result])
            ctx.prevent_default()

    async def query_server(self, server_ip_with_port: str) -> str:
        url = "http://127.0.0.1:5001/query_server"  # Flask服务器的API
        payload = {"message": f"查询服务器 {server_ip_with_port}"}
        headers = {"Content-Type": "application/json"}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    return data.get("reply", "查询失败")
                else:
                    return f"服务器查询失败，状态码: {response.status_code}"
        except Exception as e:
            self.logger.error(f"查询服务器时发生错误: {str(e)}")
            return f"查询服务器时发生错误: {str(e)}"

    def __del__(self):
        pass
