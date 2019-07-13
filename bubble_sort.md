
<script>
function reload() {
    sleep(5);
    window.href = window.locator;
}
reload();
</script>
i | j | List[i] | List[j] | swap | List | Stop  
-: | -: | -------: | -------: | ----: | ----: | ----:  
0 | 1 | None | None | None | [4,1,2,3] | i=len(List)-1  
0 | 1 | 4 | 1 | None | [4,1,2,3]  
0 | 1 | 4 | 1 | 1 | [4,1,2,3]  
0 | 1 | 4 | 4 | 1 | [4,4,2,3]  
0 | 1 | 1 | 4 | 1 | [1,4,2,3]  
0 | 2 | 1 | 2 | None | [1,4,2,3]  
0 | 3 | 1 | 3 | None | [1,4,2,3]  
1 | 2 | 4 | 2 | None | [1,4,2,3]  
1 | 2 | 4 | 2 | 2 | [1,4,2,3]  
1 | 2 | 4 | 4 | 2 | [1,4,4,3]  
1 | 2 | 2 | 4 | 2 | [1,2,4,3]  
1 | 3 | 2 | 3 | None | [1,2,4,3]  
2 | 3 | 4 | 3 | None | [1,2,4,3]  
2 | 3 | 4 | 3 | 3 | [1,2,4,3]  
2 | 3 | 4 | 4 | 3 | [1,2,4,4]  
2 | 3 | 3 | 4 | 3 | [1,2,3,4]  
3 | 4 | 4 | ? | None | [1,2,3,4]  
0 | 1 | None | None | None | [] | i=len(List)-1  
0 | 1 | None | None | None | [1] | i=len(List)-1  
0 | 1 | None | None | None | [1,1] | i=len(List)-1  
