Title: Neovim + deoplete.nvimでVue + TypeScriptの補完ができるようになりました
Tag: Vue, TypeScript
Date: 2017-08-10 11:42:03
Slug: 

できなかったので出来るように頑張りました。

![demo](https://user-images.githubusercontent.com/1256685/29148673-f6238c3a-7da9-11e7-84ee-f075adba0390.gif)

Vueファイル内で、html, typescript, cssの補完が良い感じに効くようになりました。

deoplete.nvimユーザーの方、Vue + TypeScriptが便利に書けますよ!

# やり方

deoplete.vimとcontext\_filetype.vim、nvim-typescriptを使用します。

dein.vimでプラグイン管理をする場合の最小構成は以下です。

```vim
if &compatible
  set nocompatible
endif
set runtimepath+=~/.vim/bundle/repos/github.com/Shougo/dein.vim

if dein#load_state('~/.vim/bundle')
  call dein#begin('~/.vim/bundle')

  call dein#add('Shougo/dein.vim')
  call dein#add('posva/vim-vue')
  call dein#add('Shougo/context_filetype.vim')
  "call dein#add('osyo-manga/vim-precious')
  call dein#add('Shougo/deoplete.nvim', {
  \ 'hook_add': 'let g:deoplete#enable_at_startup = 1'
  \ })
  call dein#add('mhartington/nvim-typescript', {
  \ 'hook_add': 'let g:nvim_typescript#vue_support = 1'
  \ })

  call dein#end()
  call dein#save_state()
endif

filetype plugin indent on
syntax enable
```

nvim-typescriptを使うにはまだ"npm i -g typescript"する必要があるのでそこは注意です。

# やったこと

context\_filetype.vimとnvim_typescriptをVue対応させました。



あとはdeoplete.nvim本体もShougoさんに修正した頂きました。



PRとかIssue出してから反映されるのが素早くて良い感じでした、感謝です。

色々画策しているうちに、この方法以外にもVimでVue + TypeScriptする方法はあると教えていただきました。


