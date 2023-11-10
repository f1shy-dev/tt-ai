const selectedVideos = new Set();

function updateSelectedCount() {
  const selectedCountElement = document.getElementById("selected-count");
  selectedCountElement.textContent = selectedVideos.size;
}

function compileAndOpenTab() {
  const videosArray = Array.from(selectedVideos).map((element) => [
    element.querySelector("ytd-thumbnail a").href,
    element.querySelector("#video-title").textContent,
    element.querySelector(".inline-metadata-item").textContent,
  ]);

  const jsonData = JSON.stringify(videosArray, null, 2);
  const formattedJson = `<code>${jsonData}</code>`;

  // Create a new HTML page with formatted JSON
  const newTab = window.open();
  newTab.document.write(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Formatted JSON</title>
    </head>
    <body>
      ${formattedJson}
    </body>
    </html>
  `);
}

function handleNewVideos(videoElements) {
  videoElements.forEach((element) => {
    if (selectedVideos.has(element)) {
      element.setAttribute("data-selected", "true");
    }

    element.addEventListener("click", (event) => {
      const anchor = event.target.closest("a");
      if (anchor) {
        event.preventDefault();
      }

      if (selectedVideos.has(element)) {
        element.removeAttribute("data-selected");
        selectedVideos.delete(element);
      } else {
        element.setAttribute("data-selected", "true");
        selectedVideos.add(element);
      }
      updateSelectedCount();
    });
  });
}

function importVideos() {
  const jsonData = prompt("Paste the JSON data:");
  if (jsonData) {
    try {
      const videosArray = JSON.parse(jsonData);

      // Reset selection
      selectedVideos.clear();
      // Re-highlight videos that are on the page
      videosArray.forEach((videoInfo) => {
        const url = videoInfo[0];
        const matchingElement = [
          ...document.querySelectorAll("ytd-rich-item-renderer"),
        ].find(
          (element) => element.querySelector("ytd-thumbnail a").href === url
        );

        if (matchingElement) {
          selectedVideos.add(matchingElement);
          matchingElement.setAttribute("data-selected", "true");
        } else {
          console.log(`Video not found on the page: ${url}`);
        }
      });

      alert(
        "Import successful! Check the console for videos not found on the page."
      );
    } catch (error) {
      console.error("Error parsing JSON:", error);
      alert("Invalid JSON format. Please try again.");
    }
  }
}

// Initial setup for existing videos
const videoElements = document.querySelectorAll("ytd-rich-item-renderer");
handleNewVideos(videoElements);

// MutationObserver to handle changes in the DOM (e.g., on scroll)
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === "childList") {
      const addedNodes = Array.from(mutation.addedNodes);
      const newVideoElements = addedNodes.filter(
        (node) => node.tagName === "YTD-RICH-ITEM-RENDERER"
      );
      handleNewVideos(newVideoElements);
    }
  });
});

// Configure and start the observer
const observerConfig = {
  childList: true,
  subtree: true,
};

observer.observe(document.body, observerConfig);
const toolbar = document.createElement("div");
toolbar.id = "selection-toolbar";
toolbar.innerHTML = `
  <span id="selected-count">0</span> Selected
  <button id="compile-button">Compile</button>
  <button id="import-button">Import</button>
`;
document.body.appendChild(toolbar);

const compileButton = document.getElementById("compile-button");
compileButton.addEventListener("click", compileAndOpenTab);
const importButton = document.getElementById("import-button");
importButton.addEventListener("click", importVideos);

const styles = `
  #selection-toolbar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    color: white;
    padding: 10px;
    text-align: center;
    z-index: 9999;
  }

    ytd-rich-item-renderer #content {
      pointer-events: none;
  }
  
  [data-selected] {
      filter: hue-rotate(251deg);
    background: #ffff00;
  }
`;

const styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);
