# Social preview

`social-preview.png` is a 1280 × 640 PNG of the project mark (teal pixel-art robot in a spotlight with a paper airplane) on navy. No tokens, chat ids, hosts, or tailnet names.

Keeping the file in this directory does **not** configure GitHub's social preview. GitHub has no public REST or GraphQL API to set it (POST/PUT `/repos/{owner}/{repo}/social_preview` → 404; `UpdateRepositoryInput` has no image field).

In the repository's **Settings → General → Social preview**, choose **Edit → Upload an image** and select `social-preview.png`.

See [GitHub's social-preview guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
