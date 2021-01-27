const todoInput = document.querySelector(".create_input")
const addBtn = document.querySelector(".create_button")
const todo_container = document.querySelector(".todo_container")
const todoItemClass = ["todo_item","todo_item marked", "todo_item done"]

function CreateItem(ItemTitle, ItemClassIndex){
    todo_container.insertAdjacentHTML('beforeend',`<div id="todoItem${todo_container.childElementCount+1}" class="${todoItemClass[ItemClassIndex]}">
    <div class="todo_item_header">
        <label class="checkbox_container">
            <input type="checkbox"/>
            <span class="checkmark"></span>
            <h4>${ItemTitle}</h4>
        </label>
    </div>
    <div class="todo_item_footer">
        <p>${new Date().toLocaleDateString()}<span> ${new Date().toLocaleTimeString()}</span></p>
        <div class="action_buttons">
            <img onclick="DeleteItem(${todo_container.childElementCount+1})" src="{% static 'img/basket.png' %}" alt="">
            ${ItemClassIndex === 1 ? `<img onclick="PickedItem(${todo_container.childElementCount+1})" src="./img/yellow.png" alt="">` : `<img onclick="PickedItem(${todo_container.childElementCount+1})" src="./img/star.png" alt="">`}
        </div>
    </div>
</div>`);
}

function DeleteItem(e){
    console.log("qwe : "+e)
    todo_container.querySelector("#todoItem"+e).remove()
}
function PickedItem(e){
    console.log("qwe : "+e)
    var item = todo_container.querySelector("#todoItem"+e)
    if(item.className == todoItemClass[0])
    {
        item.className = todoItemClass[1]
        item.children[1].children[1].children[1].outerHTML = `<img onclick="PickedItem(${e})" src="./img/yellow.png" alt="">`    
    }
    else
    {
        item.className = todoItemClass[0]
        item.children[1].children[1].children[1].outerHTML = `<img onclick="PickedItem(${e})" src="./img/star.png" alt="">`    
    }
}

CreateItem("Milk",0)
CreateItem("Coffee",1)
CreateItem("Chocolate",2)

addBtn.addEventListener("click", function(){
    if(todoInput.value == ''){
        alert('Error')
    }
    else
    CreateItem(todoInput.value, 0)
    todoInput.value = ''
    console.log(todo_container.childElementCount)
})