from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    try:
        # Langflow setup
        flow_id_or_name = 'aed37c10-7ac1-4cf5-9fcd-7c08fb469135'
        langflow_id = '04c10269-3dde-497c-b20f-9ecb31f155db'
        application_token = 'AstraCS:CnDgpfCjLZgcxFWZbxbhWsyZ:c374c393102f859c46633a6c919ab7f8bf83b4c4c83e55b331dcfe8b21c6e855'
        langflow_client = LangflowClient('https://api.langflow.astra.datastax.com', application_token)

        # Prepare tweaks (if necessary)
        tweaks = {
            "ChatInput-n0p3k": {},
            "Prompt-qJyGE": {},
            "AstraDBToolComponent-2bEY8": {},
            "Agent-XtCvF": {},
            "ChatOutput-g0GbU": {}
        }

        # Fetch chat data
        chat_input_value = "Fetch chat-related data"
        chat_data = langflow_client.run_flow(
            flow_id_or_name,
            langflow_id,
            chat_input_value,
            "chat",
            "chat",
            tweaks,
            stream=False
        )

        # Fetch graph data
        graph_input_value = "Fetch graph-related data"
        graph_data = langflow_client.run_flow(
            flow_id_or_name,
            langflow_id,
            graph_input_value,
            "chat",
            "chat",
            tweaks,
            stream=False
        )

        # Return the combined data for both templates
        context = {
            'chat_data': chat_data,
            'graph_data': graph_data
        }

        # Default to index.html (optional)
        return render(request, "window/index.html", context)

    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch data: {str(e)}"}, status=500)


def chat_view(request):
    try:
        # Fetch chat-specific data
        flow_id_or_name = 'aed37c10-7ac1-4cf5-9fcd-7c08fb469135'
        langflow_id = '04c10269-3dde-497c-b20f-9ecb31f155db'
        application_token = 'AstraCS:CnDgpfCjLZgcxFWZbxbhWsyZ:c374c393102f859c46633a6c919ab7f8bf83b4c4c83e55b331dcfe8b21c6e855'
        langflow_client = LangflowClient('https://api.langflow.astra.datastax.com', application_token)

        # Prepare tweaks (if any)
        tweaks = {
            "ChatInput-n0p3k": {},
            "Prompt-qJyGE": {},
            "AstraDBToolComponent-2bEY8": {},
            "Agent-XtCvF": {},
            "ChatOutput-g0GbU": {}
        }

        # Fetch chat data
        chat_input_value = "Fetch chat-related data"
        chat_data = langflow_client.run_flow(
            flow_id_or_name,
            langflow_id,
            chat_input_value,
            "chat",
            "chat",
            tweaks,
            stream=False
        )

        context = {
            'chat_data': chat_data
        }
        return render(request, 'window/chat.html', context)

    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch chat data: {str(e)}"}, status=500)


def graph_view(request):
    try:
        # Fetch graph-specific data
        flow_id_or_name = 'aed37c10-7ac1-4cf5-9fcd-7c08fb469135'
        langflow_id = '04c10269-3dde-497c-b20f-9ecb31f155db'
        application_token = 'AstraCS:CnDgpfCjLZgcxFWZbxbhWsyZ:c374c393102f859c46633a6c919ab7f8bf83b4c4c83e55b331dcfe8b21c6e855'
        langflow_client = LangflowClient('https://api.langflow.astra.datastax.com', application_token)

        # Prepare tweaks (if any)
        tweaks = {
            "ChatInput-n0p3k": {},
            "Prompt-qJyGE": {},
            "AstraDBToolComponent-2bEY8": {},
            "Agent-XtCvF": {},
            "ChatOutput-g0GbU": {}
        }

        # Fetch graph data
        graph_input_value = "Fetch graph-related data"
        graph_data = langflow_client.run_flow(
            flow_id_or_name,
            langflow_id,
            graph_input_value,
            "chat",
            "chat",
            tweaks,
            stream=False
        )

        context = {
            'graph_data': graph_data
        }
        return render(request, 'window/graphs.html', context)

    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch graph data: {str(e)}"}, status=500)


