var updateBtns = document.getElementsByClassName('update-basket')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var menuID = this.dataset.menu
        var action = this.dataset,action
        console.log('menuID:',menuID,'action:',action)
    })
}
