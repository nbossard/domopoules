
" Launch NERDTree at start and custom startify
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | wincmd l | endif

" special colorscheme for backend
colorscheme dracula
set background=light

