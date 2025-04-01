document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchMatura');
    const levelButtons = document.querySelectorAll('#filterGroupLevel .filter-btn');
    const publisherButtons = document.querySelectorAll('#filterGroupPublisher .filter-btn');
    const tableRows = document.querySelectorAll('#tableMatura tbody tr');
    
    function filterTable() {
        const searchText = searchInput.value.toLowerCase();
        const activeLevel = document.querySelector('#filterGroupLevel .filter-btn.active')?.dataset.level;
        const activePublisher = document.querySelector('#filterGroupPublisher .filter-btn.active')?.dataset.publisher;
        
        tableRows.forEach(row => {
            const date = row.cells[0].textContent.toLowerCase();
            const type = row.cells[1].textContent.toLowerCase();
            const publisher = row.cells[2].textContent;
            const level = row.dataset.level;
            
            const matchesSearch = date.includes(searchText) || type.includes(searchText);
            const matchesLevel = !activeLevel || level === activeLevel;
            const matchesPublisher = !activePublisher || publisher === activePublisher;
            
            row.style.display = matchesSearch && matchesLevel && matchesPublisher ? '' : 'none';
        });
    }
    
    searchInput.addEventListener('input', filterTable);
    
    levelButtons.forEach(button => {
        button.addEventListener('click', function() {
            levelButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            filterTable();
        });
    });
    
    publisherButtons.forEach(button => {
        button.addEventListener('click', function() {
            publisherButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            filterTable();
        });
    });
    
    // Inicjalne filtrowanie - pokazuj tylko rozszerzony
    filterTable();
}); 