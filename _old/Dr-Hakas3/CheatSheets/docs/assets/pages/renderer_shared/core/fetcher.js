export async function loadJson(path) {
  try {
    const response = await fetch(path);

    if (!response.ok) {
      throw new Error(`Failed to load JSON: ${path}`);
    }

    return await response.json();
  } catch (error) {
    console.error("[fetcher.js] JSON Load Error:", error);
    return [];
  }
}

export async function loadText(path) {
  try {
    const response = await fetch(path);

    if (!response.ok) {
      throw new Error(`Failed to load text: ${path}`);
    }

    return await response.text();
  } catch (error) {
    console.error("[fetcher.js] Text Load Error:", error);
    return "";
  }
}
