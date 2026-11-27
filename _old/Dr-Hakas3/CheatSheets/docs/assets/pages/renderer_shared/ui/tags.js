export function renderTagList({
  tags = [],
  containerId = "tags"
}) {
  const container = document.getElementById(containerId);

  if (!container) {
    console.error(`[tags.js] Container not found: ${containerId}`);
    return;
  }

  container.innerHTML = "";

  tags.forEach((tag) => {
    const element = document.createElement("span");

    element.className = "tag";
    element.innerText = `#${tag}`;

    container.appendChild(element);
  });
}
