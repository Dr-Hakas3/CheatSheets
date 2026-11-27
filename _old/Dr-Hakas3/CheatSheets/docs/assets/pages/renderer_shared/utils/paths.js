const isGithubPages =
  window.location.hostname.includes("github.io");

export const BASE_PATH = isGithubPages
  ? "/CheatSheets"
  : "";

export function normalizePath(path = "") {
  if (!path.startsWith("/")) {
    path = "/" + path;
  }

  return path;
}

export function buildAssetPath(path = "") {
  return `${BASE_PATH}${normalizePath(path)}`;
}

export function buildMarkdownPath(path = "") {
  return `${BASE_PATH}${normalizePath(path)}`;
}

export function buildJsonPath(path = "") {
  return `${BASE_PATH}${normalizePath(path)}`;
}

export function currentPath() {
  return window.location.pathname;
}
