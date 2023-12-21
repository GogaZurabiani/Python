with open("sample_server_log.txt", "r") as f1:
    Repeated = {'settings': "http://example.com/settings", "contact": "http://example.com/contact",
                "home": 'http://example.com/home', "profile": 'http://example.com/profile',
                "login": 'http://example.com/login', "about": 'http://example.com/about'}

    setting = 0
    for line in f1:
        if line.startswith("INFO: Accessed URL:"):
            url = line.split('INFO: Accessed URL:')[1].strip()
            print(url)

            # Check if the 'settings' URL is in the current line
            if Repeated['settings'] in url:
                setting += 1

    print(f"The 'settings' URL appears {setting} times.")
