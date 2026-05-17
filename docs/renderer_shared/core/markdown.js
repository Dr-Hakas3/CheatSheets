import { loadText } from "./fetcher.js";

export async function renderMarkdown({
  markdownPath,
  containerId
}) {
  const container = document.getElementById(containerId);

  if (!container) {
    console.error(`[markdown.js] Container not found: ${containerId}`);
    return;
  }

  const markdown = await loadText(markdownPath);

  if (!markdown) {
    container.innerHTML = `
      <div class="error">
        Failed to load markdown.
      </div>
    `;
    return;
  }

  if (typeof marked === "undefined") {
    console.error("[markdown.js] marked.js is not loaded.");
    container.innerHTML = `
      <div class="error">
        marked.js not loaded.
      </div>
    `;
    return;
  }

  container.innerHTML = marked.parse(markdown);

  enhanceCodeBlocks(container);
}

function enhanceCodeBlocks(container) {
  const codeBlocks = container.querySelectorAll("pre code");

  codeBlocks.forEach((block) => {
    const pre = block.parentElement;

    const wrapper = document.createElement("div");
    wrapper.className = "codeblock-wrapper";

    const button = document.createElement("button");
    button.className = "copy-button";
    button.innerText = "Copy";

    button.onclick = async () => {
      try {
        await navigator.clipboard.writeText(block.innerText);

        button.innerText = "Copied!";

        setTimeout(() => {
          button.innerText = "Copy";
        }, 1500);
      } catch (error) {
        console.error("[markdown.js] Copy failed:", error);
      }
    };

    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(button);
    wrapper.appendChild(pre);
  });
}
