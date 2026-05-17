export function setupSearch({
  inputId,
  data = [],
  onResults
}) {
  const input = document.getElementById(inputId);

  if (!input) {
    console.error(`[search.js] Input not found: ${inputId}`);
    return;
  }

  input.addEventListener("input", () => {
    const keyword = input.value.toLowerCase();

    const filtered = data.filter((item) => {
      const title = (item.title || "").toLowerCase();

      const description = (
        item.description || ""
      ).toLowerCase();

      const tags = (item.tags || [])
        .join(" ")
        .toLowerCase();

      return (
        title.includes(keyword) ||
        description.includes(keyword) ||
        tags.includes(keyword)
      );
    });

    onResults(filtered);
  });
}
