import http.client
import json

GH_API_HOST = "api.github.com"


def get_all_releases(repo_owner, repo_name, token=None):
    conn = http.client.HTTPSConnection(GH_API_HOST)
    if token:
        headers = {'Authorization': f'token {token}', 'User-Agent': 'Python'}
    else:
        headers = {'User-Agent': 'Python'}
    page = 1
    per_page = 100  # 每页返回 100 个结果，根据需要进行调整
    releases = []

    while True:
        url = f"/repos/{repo_owner}/{repo_name}/releases?page={page}&per_page={per_page}"
        conn.request("GET", url, headers=headers)
        response = conn.getresponse()
        data = response.read()

        if response.status // 100 != 2:
            raise Exception(f"Request failed: {response.status}, {data.decode()}")

        page_releases = json.loads(data.decode())

        if not page_releases:
            break

        releases.extend(page_releases)
        page += 1

    conn.close()
    return releases


# if __name__ == '__main__':
#     owner = "radxa-build"
#     repo = "rock-5b"
#     token = None  # 如果需要身份验证，请设置为您的 GitHub 访问令牌
#
#     all_releases = get_all_releases(owner, repo, token)
#     for release in all_releases:
#         print(release['tag_name'])
#     print(len(all_releases))