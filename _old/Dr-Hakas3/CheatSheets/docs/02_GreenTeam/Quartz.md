## Step 1

```zsh
node --version
npm --version
```

12.2以上ならOK


```zsh
cd ~/Desktop
git clone https://github.com/jackyzha0/quartz.git Quartz
cd Quartz
npm i
```

```zsh
npx quartz create
npm notice run @jackyzha0/quartz@5.1.0 npx
npm notice run 'quartz' create

┌   Quartz v5.1.0 
│
◇  Choose a template for your Quartz configuration
│  Obsidian
│
◇  Choose how to initialize the content in `/home/kali/Desktop/CheatSheets-site/content`
│  Symlink an existing folder
│
◇  Enter the full path to existing content folder
│  /home/kali/Desktop/Study/CheatSheets
│
◇  Enter the base URL for your Quartz site (e.g. mysite.github.io/quartz)
│  /home/kali/Desktop/Study/CheatSheets
Created quartz.config.yaml from 'obsidian' template
Found 1 npm plugin(s) in config that are not installed:

  @quartz-community/obsidian-plugin-excalidraw


added 8 packages, and audited 428 packages in 4s

152 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
npm warn install-scripts 2 packages had install scripts blocked because they are not covered by allowScripts:
npm warn install-scripts   @parcel/watcher@2.6.0 (install: node-gyp rebuild)
npm warn install-scripts   esbuild@0.28.2 (postinstall: node install.js)
npm warn install-scripts
npm warn install-scripts Run `npm install-scripts ls` to review, or `npm install-scripts approve <pkg>` to allow.
✓ Installed 1 npm plugin(s)

✓ All configured plugins are already installed
│
└  You're all set! Not sure what to do next? Try:
  • Customizing Quartz a bit more by editing `quartz.config.yaml`
  • Running `npx quartz build --serve` to preview your Quartz locally
  • Hosting your Quartz online (see: https://quartz.jzhao.xyz/hosting)
```

![[Pasted image 20261114020045.png]]