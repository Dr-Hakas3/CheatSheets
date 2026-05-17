export function openModal(content = "") {
  closeModal();

  const overlay = document.createElement("div");
  overlay.className = "modal-overlay";
  overlay.id = "shared-modal-overlay";

  const modal = document.createElement("div");
  modal.className = "modal";

  modal.innerHTML = `
    <button class="modal-close">
      ×
    </button>

    <div class="modal-content">
      ${content}
    </div>
  `;

  overlay.appendChild(modal);

  document.body.appendChild(overlay);

  const closeButton = modal.querySelector(".modal-close");

  closeButton.addEventListener("click", closeModal);

  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) {
      closeModal();
    }
  });

  document.addEventListener("keydown", escapeHandler);
}

export function closeModal() {
  const existing = document.getElementById(
    "shared-modal-overlay"
  );

  if (existing) {
    existing.remove();
  }

  document.removeEventListener(
    "keydown",
    escapeHandler
  );
}

function escapeHandler(event) {
  if (event.key === "Escape") {
    closeModal();
  }
}
