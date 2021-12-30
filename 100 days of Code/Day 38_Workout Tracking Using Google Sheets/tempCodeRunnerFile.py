bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )