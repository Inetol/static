const content = $('body > div.container > div > div');
let table = $('table', content);
const hasHTML = false;

function replaceBreadcrumbs() {
    const breadcrumb = content[0].childNodes[1];
    let breadcrumbHTML = '<nav aria-label="breadcrumb"><ol class="breadcrumb" id="breadcrumb">';
    const bits = breadcrumb.textContent.trim().replace(/\/$/, '').split('/');
    let path = '';

    bits.forEach(function (item, idx) {
        path += item + '/';

        if (idx === 0) item = 'home';
        if (idx === bits.length - 1) breadcrumbHTML += '<li class="breadcrumb-item active" aria-current="page">' + item + '</li>';
        else breadcrumbHTML += '<li class="breadcrumb-item"><a href="' + path + '">' + item + '</a></li>';
    });

    breadcrumbHTML += '</ol></nav>';
    content[0].replaceChild($(breadcrumbHTML)[0], breadcrumb);
}

function fixTable() {
    table = $('#list');

    table.removeAttr("cellpadding");
    table.removeAttr("cellspacing");
    table.addClass(['table', 'table-sm', 'table-hover', 'text-nowrap', 'table-striped', 'table-borderless']);

    const header = $('tr', table)[0];
    const thead = $('<thead>');

    header.remove();
    thead.addClass(['thead-dark']);
    thead.append(header);
    table.prepend(thead);
    $(header).prepend($('<th class="col-auto"></th>'));
    $('th:gt(1)', header).addClass(['col-auto', 'd-none', 'd-md-table-cell']);

    $('a[href^="../"]', table).closest('tr').remove();

    $('tbody tr', table).each(function () {
        const icon = $('<td></td>');
        const filename = $('td:first a', this).attr('href').replace(/\?.*$/, '');
        let iconName;

        icon.addClass(['col-auto']);
        if (filename.endsWith('/')) iconName = 'fas fa-folder';
        else iconName = 'far fa-file-alt';

        icon.append($('<i class="' + iconName + '" aria-hidden="true"></i>'));
        $(this).prepend(icon);

        $('td:gt(1)', this).addClass(['col-auto', 'd-none', 'd-md-table-cell']);
        $('td:eq(1)', this).addClass(['col']);
    });
}

$(function () {
    try {
        if (!hasHTML) {
            replaceBreadcrumbs();
            fixTable();
        }
    } finally {
        $('#mainContent').show();
    }
});
