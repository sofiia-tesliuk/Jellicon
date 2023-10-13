function chooseBubble() {
    let index = Math.floor(Math.random() * 6);
    let choices = ['bubble_1', 'bubble_1', 'bubble_1', 'bubble_2', 'bubble_3', 'bubble_4'];
    return choices[index]
}

function createBubble(){
    const section = document.querySelector('.main');
    const newBubble = document.createElement('span');
    newBubble.classList.add('bubble');
    newBubble.classList.add(chooseBubble());

    const randomSpeed = Math.floor(Math.random() * 4000 + 6000);
    newBubble.style.animationDuration = randomSpeed + 'ms';

    newBubble.style.left = Math.random() * innerWidth - 32 + 'px';
    section.appendChild(newBubble);

    setTimeout(() => {
        newBubble.remove()
    }, 6000)
}

setInterval(createBubble, 100);