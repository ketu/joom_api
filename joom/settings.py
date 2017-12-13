from urllib.parse import urljoin

BASE_URL = "https://api-merchant.joom.com/"

BASE_ENDPOINT = "api/v2/"

FULL_BASE_URL = urljoin(BASE_URL, BASE_ENDPOINT)

BASE_AUTHORIZATION_URL = urljoin(FULL_BASE_URL, "oauth/authorize")

BASE_ACCESS_TOKEN_URL = urljoin(FULL_BASE_URL, "oauth/access_token")

BASE_REFRESH_TOKEN_URL = urljoin(FULL_BASE_URL, "oauth/refresh_token")
