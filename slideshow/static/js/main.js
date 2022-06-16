M.AutoInit();

document.addEventListener('DOMContentLoaded', function () {
    const elems = document.querySelectorAll('.fixed-action-btn');
    const fbtn_instances = M.FloatingActionButton.init(elems, {
        hoverEnabled: false
    });
});


