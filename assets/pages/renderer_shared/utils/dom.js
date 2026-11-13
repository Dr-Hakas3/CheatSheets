export function clearElement(element) {
  if (!element) {
    return;
  }

  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}

export function createElement({
  tag = "div",
  className = "",
  text = "",
  html = ""
}) {
  const element = document.createElement(tag);

  if (className) {
    element.className = className;
  }

  if (text) {
    element.innerText = text;
  }

  if (html) {
    element.innerHTML = html;
  }

  return element;
}

export function getElement(id) {
  const element = document.getElementById(id);

  if (!element) {
    console.error(`[dom.js] Element not found: ${id}`);
  }

  return element;
}

export function showElement(element) {
  if (!element) {
    return;
  }

  element.classList.remove("hidden");
}

export function hideElement(element) {
  if (!element) {
    return;
  }

  element.classList.add("hidden");
}
