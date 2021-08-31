You need to get your credentials from the GCP console and rename it
as `client_secrets.json` before executing your code.

Steps:
1. Execute `authentication.py` and authenticate your host machine. This way you get a `credentials_module.json` file
so your session never expires.
2. Create a `settings.yaml` (use the `settings.yaml.template` as a guide) and fill `client_id` and `client_secret` fileds.
3. You now can use the `gdrive.py` file to create, update, delete, give permissions to your files 
(Be sure to check PyDrive2 documentation)

Video example:
+ [How To Get `client_secrets.json` file Tutorial](https://www.youtube.com/watch?v=pHhIICVcI6s)