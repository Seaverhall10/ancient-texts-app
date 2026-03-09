// Generate a simple app icon as a PNG (256x256)
// For production, replace with a professional icon designed in an image editor.
// This creates a dark background with a gold scroll/book symbol.

const fs = require('fs');
const path = require('path');

// Minimal BMP/ICO generator for a 256x256 icon
// Creates a simple dark+gold branded icon

function createIcon() {
  const size = 256;
  const pixels = Buffer.alloc(size * size * 4); // RGBA

  // Colors
  const bg = [12, 14, 20, 255];       // --bg-primary
  const gold = [201, 168, 76, 255];    // --gold
  const goldDim = [100, 84, 38, 255];  // dimmed gold

  // Fill background
  for (let i = 0; i < size * size; i++) {
    pixels[i * 4] = bg[0];
    pixels[i * 4 + 1] = bg[1];
    pixels[i * 4 + 2] = bg[2];
    pixels[i * 4 + 3] = bg[3];
  }

  function setPixel(x, y, color) {
    if (x < 0 || x >= size || y < 0 || y >= size) return;
    const idx = (y * size + x) * 4;
    pixels[idx] = color[0];
    pixels[idx + 1] = color[1];
    pixels[idx + 2] = color[2];
    pixels[idx + 3] = color[3];
  }

  function fillCircle(cx, cy, r, color) {
    for (let y = cy - r; y <= cy + r; y++) {
      for (let x = cx - r; x <= cx + r; x++) {
        if ((x - cx) * (x - cx) + (y - cy) * (y - cy) <= r * r) {
          setPixel(Math.round(x), Math.round(y), color);
        }
      }
    }
  }

  function fillRect(x1, y1, x2, y2, color) {
    for (let y = y1; y <= y2; y++) {
      for (let x = x1; x <= x2; x++) {
        setPixel(x, y, color);
      }
    }
  }

  // Draw a rounded border ring
  const center = size / 2;
  for (let angle = 0; angle < Math.PI * 2; angle += 0.001) {
    for (let r = 118; r <= 124; r++) {
      const x = Math.round(center + r * Math.cos(angle));
      const y = Math.round(center + r * Math.sin(angle));
      setPixel(x, y, goldDim);
    }
  }

  // Draw a stylized open scroll/book shape
  // Left page
  for (let y = 70; y <= 186; y++) {
    const curvature = Math.sin((y - 70) / 116 * Math.PI) * 12;
    const x1 = Math.round(60 - curvature);
    const x2 = 124;
    for (let x = x1; x <= x2; x++) {
      setPixel(x, y, goldDim);
    }
  }

  // Right page
  for (let y = 70; y <= 186; y++) {
    const curvature = Math.sin((y - 70) / 116 * Math.PI) * 12;
    const x1 = 132;
    const x2 = Math.round(196 + curvature);
    for (let x = x1; x <= x2; x++) {
      setPixel(x, y, goldDim);
    }
  }

  // Spine (center binding)
  fillRect(124, 68, 132, 188, gold);

  // Text lines on left page (decorative)
  for (let line = 0; line < 7; line++) {
    const y = 88 + line * 14;
    const width = 40 + Math.random() * 20;
    fillRect(72, y, Math.round(72 + width), y + 2, [201, 168, 76, 120]);
  }

  // Text lines on right page (decorative)
  for (let line = 0; line < 7; line++) {
    const y = 88 + line * 14;
    const width = 40 + Math.random() * 20;
    fillRect(140, y, Math.round(140 + width), y + 2, [201, 168, 76, 120]);
  }

  // Cross at the top center of the book (small)
  fillRect(125, 56, 131, 70, gold);
  fillRect(121, 60, 135, 64, gold);

  // Write as simple BMP embedded in ICO
  // ICO format: header + directory entry + BMP data
  const bmpInfoSize = 40;
  const bmpDataSize = size * size * 4;
  const bmpSize = bmpInfoSize + bmpDataSize;

  // ICO header (6 bytes)
  const icoHeader = Buffer.alloc(6);
  icoHeader.writeUInt16LE(0, 0);     // reserved
  icoHeader.writeUInt16LE(1, 2);     // ICO type
  icoHeader.writeUInt16LE(1, 4);     // 1 image

  // ICO directory entry (16 bytes)
  const icoDir = Buffer.alloc(16);
  icoDir.writeUInt8(0, 0);           // width (0 = 256)
  icoDir.writeUInt8(0, 1);           // height (0 = 256)
  icoDir.writeUInt8(0, 2);           // color palette
  icoDir.writeUInt8(0, 3);           // reserved
  icoDir.writeUInt16LE(1, 4);        // color planes
  icoDir.writeUInt16LE(32, 6);       // bits per pixel
  icoDir.writeUInt32LE(bmpSize, 8);  // data size
  icoDir.writeUInt32LE(22, 12);      // offset to data (6 + 16 = 22)

  // BMP info header (40 bytes)
  const bmpInfo = Buffer.alloc(40);
  bmpInfo.writeUInt32LE(40, 0);          // header size
  bmpInfo.writeInt32LE(size, 4);         // width
  bmpInfo.writeInt32LE(size * 2, 8);     // height (doubled for ICO convention)
  bmpInfo.writeUInt16LE(1, 12);          // planes
  bmpInfo.writeUInt16LE(32, 14);         // bits per pixel
  bmpInfo.writeUInt32LE(0, 16);          // compression (none)
  bmpInfo.writeUInt32LE(bmpDataSize, 20);// image size
  bmpInfo.writeInt32LE(0, 24);           // h resolution
  bmpInfo.writeInt32LE(0, 28);           // v resolution
  bmpInfo.writeUInt32LE(0, 32);          // colors used
  bmpInfo.writeUInt32LE(0, 36);          // important colors

  // BMP pixel data (bottom-up, BGRA)
  const bmpData = Buffer.alloc(bmpDataSize);
  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      const srcIdx = ((size - 1 - y) * size + x) * 4; // flip vertically
      const dstIdx = (y * size + x) * 4;
      bmpData[dstIdx] = pixels[srcIdx + 2];     // B
      bmpData[dstIdx + 1] = pixels[srcIdx + 1]; // G
      bmpData[dstIdx + 2] = pixels[srcIdx];     // R
      bmpData[dstIdx + 3] = pixels[srcIdx + 3]; // A
    }
  }

  const ico = Buffer.concat([icoHeader, icoDir, bmpInfo, bmpData]);
  const outPath = path.join(__dirname, 'icon.ico');
  fs.writeFileSync(outPath, ico);
  console.log(`Icon written to ${outPath} (${ico.length} bytes)`);
}

createIcon();
