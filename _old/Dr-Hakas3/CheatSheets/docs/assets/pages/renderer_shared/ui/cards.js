import { goTo } from "../core/router.js";

export function renderCards({
  data = [],
  containerId = "cards"
}) {

  const container =
    document.getElementById(containerId);

  if (!container) {
    console.error(
      `[cards.js] Container not found: ${containerId}`
    );
    return;
  }

  container.innerHTML = "";

  if (!Array.isArray(data) || data.length === 0) {

    container.innerHTML = `
      <div class="error">
        No data found.
      </div>
    `;

    return;
  }

  const grid = document.createElement("div");

  grid.className = "card-grid";

  data.forEach((item) => {

    const card = createCard(item);

    grid.appendChild(card);

  });

  container.appendChild(grid);

}

function createCard(item) {

  const card =
    document.createElement("div");

  card.className = "card";

  const difficulty =
    (item.difficulty || "")
      .toLowerCase();

  card.innerHTML = `

    <div class="card-body">

      <h2 class="card-title">
        ${item.title || "Untitled"}
      </h2>

      <p class="card-description">
        ${item.description || ""}
      </p>

    </div>

    <div class="card-footer">

      ${
        item.difficulty
          ? `
            <div class="card-difficulty ${difficulty}">
              ${item.difficulty}
            </div>
          `
          : ""
      }

      ${renderTags(item.tags)}

    </div>
  `;

  if (item.path) {

    card.addEventListener("click", () => {
      goTo(item.path);
    });

  }

  return card;

}

function renderTags(tags = []) {

  if (
    !Array.isArray(tags) ||
    tags.length === 0
  ) {
    return "";
  }

  return `
    <div class="card-tags">

      ${tags.map(tag => `
        <span class="card-tag">
          ${tag}
        </span>
      `).join("")}

    </div>
  `;

}
