


function hardWork(number) {
    j = 0;
    for (i = 0; i < number; i++) {
        j = j + i*i;
    }
    return j;
}

process.on('message', message => {
    const result = hardWork(message);
    process.send(result);
});