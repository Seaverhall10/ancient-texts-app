// Preload script — runs in renderer context before page scripts.
// Provides a secure bridge between the Electron main process and the web page.
// Currently minimal since the app is self-contained HTML.

const { contextBridge } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  isElectron: true,
  platform: process.platform,
});
