const isGithubPages = window.location.hostname.includes("github.io");

export const BASE_PATH = isGithubPages
  ? "/CheatSheets"
  : "";

export function buildPath(path = "") {
  if (!path.startsWith("/")) {
    path = "/" + path;
  }

  return `${BASE_PATH}${path}`;
}

export function goTo(path) {
  window.location.href = buildPath(path);
}
