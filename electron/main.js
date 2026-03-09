const { app, BrowserWindow, Menu, shell } = require('electron');
const path = require('path');

// Keep a global reference to avoid garbage collection
let mainWindow;

// Resolve the HTML file path
function getHtmlPath() {
  if (app.isPackaged) {
    // In production: file is in resources/app/
    return path.join(process.resourcesPath, 'app', 'AncientTextsStudy.html');
  }
  // In development: file is in ../output/
  return path.join(__dirname, '..', 'output', 'AncientTextsStudy.html');
}

// Window state persistence
const STATE_FILE = 'window-state.json';
const fs = require('fs');

function loadWindowState() {
  try {
    const statePath = path.join(app.getPath('userData'), STATE_FILE);
    if (fs.existsSync(statePath)) {
      return JSON.parse(fs.readFileSync(statePath, 'utf8'));
    }
  } catch (e) {
    // ignore
  }
  return { width: 1400, height: 900 };
}

function saveWindowState(win) {
  try {
    const bounds = win.getBounds();
    const isMaximized = win.isMaximized();
    const statePath = path.join(app.getPath('userData'), STATE_FILE);
    fs.writeFileSync(statePath, JSON.stringify({ ...bounds, isMaximized }));
  } catch (e) {
    // ignore
  }
}

function createWindow() {
  const state = loadWindowState();

  mainWindow = new BrowserWindow({
    width: state.width,
    height: state.height,
    x: state.x,
    y: state.y,
    minWidth: 800,
    minHeight: 600,
    backgroundColor: '#0c0e14',
    title: 'Ancient Texts Study',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
    show: false,
  });

  if (state.isMaximized) {
    mainWindow.maximize();
  }

  // Build the application menu
  const menuTemplate = buildMenu();
  Menu.setApplicationMenu(Menu.buildFromTemplate(menuTemplate));

  // Load the HTML file
  const htmlPath = getHtmlPath();
  mainWindow.loadFile(htmlPath);

  // Show window when ready (avoids white flash)
  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
  });

  // Save state on close
  mainWindow.on('close', () => {
    saveWindowState(mainWindow);
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  // Open external links in default browser
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

function buildMenu() {
  return [
    {
      label: 'File',
      submenu: [
        {
          label: 'Reload',
          accelerator: 'CmdOrCtrl+R',
          click: () => mainWindow && mainWindow.reload(),
        },
        { type: 'separator' },
        { role: 'quit' },
      ],
    },
    {
      label: 'Edit',
      submenu: [
        { role: 'copy' },
        { role: 'selectAll' },
        { type: 'separator' },
        {
          label: 'Find...',
          accelerator: 'CmdOrCtrl+F',
          click: () => {
            // Trigger the app's built-in search
            mainWindow && mainWindow.webContents.executeJavaScript(
              `document.querySelector('.search-input')?.focus()`
            );
          },
        },
      ],
    },
    {
      label: 'View',
      submenu: [
        {
          label: 'Zoom In',
          accelerator: 'CmdOrCtrl+Plus',
          click: () => {
            const wc = mainWindow.webContents;
            wc.setZoomLevel(wc.getZoomLevel() + 0.5);
          },
        },
        {
          label: 'Zoom Out',
          accelerator: 'CmdOrCtrl+-',
          click: () => {
            const wc = mainWindow.webContents;
            wc.setZoomLevel(wc.getZoomLevel() - 0.5);
          },
        },
        {
          label: 'Reset Zoom',
          accelerator: 'CmdOrCtrl+0',
          click: () => {
            mainWindow.webContents.setZoomLevel(0);
          },
        },
        { type: 'separator' },
        { role: 'togglefullscreen' },
        { type: 'separator' },
        {
          label: 'Developer Tools',
          accelerator: 'F12',
          click: () => mainWindow && mainWindow.webContents.toggleDevTools(),
        },
      ],
    },
    {
      label: 'Navigate',
      submenu: [
        {
          label: 'Library (Home)',
          accelerator: 'Alt+H',
          click: () => {
            mainWindow && mainWindow.webContents.executeJavaScript(
              `typeof showLibrary === 'function' && showLibrary()`
            );
          },
        },
        {
          label: 'Search',
          accelerator: 'CmdOrCtrl+K',
          click: () => {
            mainWindow && mainWindow.webContents.executeJavaScript(
              `document.querySelector('.search-input')?.focus()`
            );
          },
        },
        { type: 'separator' },
        {
          label: 'Toggle Reading Pane',
          accelerator: 'Alt+R',
          click: () => {
            mainWindow && mainWindow.webContents.executeJavaScript(
              `typeof toggleReadingPane === 'function' && toggleReadingPane()`
            );
          },
        },
        {
          label: 'Toggle Sidebar',
          accelerator: 'Alt+S',
          click: () => {
            mainWindow && mainWindow.webContents.executeJavaScript(
              `typeof toggleSidebar === 'function' && toggleSidebar()`
            );
          },
        },
      ],
    },
    {
      label: 'Help',
      submenu: [
        {
          label: 'About Ancient Texts Study',
          click: () => {
            const { dialog } = require('electron');
            dialog.showMessageBox(mainWindow, {
              type: 'info',
              title: 'Ancient Texts Study',
              message: 'Ancient Texts Study App',
              detail: `Version ${app.getVersion()}\n\nDeep scripture study with original languages,\ncross-references, and divine council theology.\n\nBuilt by Seaver Hall`,
            });
          },
        },
      ],
    },
  ];
}

// App lifecycle
app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  app.quit();
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
