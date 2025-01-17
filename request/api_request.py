# api_request.py
from dashscope import Application

def get_response(api_key, app_id, messages, workspace, max_tokens=200):
    """
    调用 DashScope API，发送消息并获取回复。
    :param api_key: API Key
    :param app_id: 应用 ID
    :param messages: 消息列表，例如：[("用户", "问题内容")]
    :param workspace: 工作区
    :param max_tokens: 最大生成的回答长度
    :return: API 返回的回答
    """
    # Join all messages into a single prompt
    prompt = "\n".join([f"{sender}: {msg}" for sender, msg in messages])
    try:
        # 确保 api_key 和 app_id 不为空
        if not api_key or not app_id:
            return "API Key 或 App ID 未填写，请检查设置！"

        response = Application.call(
            api_key=api_key,
            app_id=app_id,
            workspace=workspace,
            prompt=prompt,
            max_tokens=max_tokens  # 限制生成文本的长度
        )
        if response.output and hasattr(response.output, "text"):
            return response.output.text
        else:
            return "未能从助手中获取有效回复，请稍后再试。"
    except Exception as e:
        return f"调用 API 时发生错误: {str(e)}"

