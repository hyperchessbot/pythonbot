import os

keys = [
  "GITHUB_PUSH_TOKEN",
  "GITLAB_PUSH_TOKEN",
  "RUST_BOT_TOKEN"
]

with open("e", "w") as outfile:
  for k in keys:    
    outfile.write(f'export {k}={os.getenv(k)}\n')

