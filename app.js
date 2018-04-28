var search = instantsearch({
  // Replace with your own values
  appId: '4XE5Z25BS5',
  apiKey: '62506859dce690b1cc5aadd634e8999e', // search only API key, no ADMIN key
  indexName: 'idx_mt101',
  urlSync: true,
  searchParameters: {
    hitsPerPage: 10
  }
});

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-input'
  })
);


search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
    },
    cssClasses: {
      root: 'row'
      ,item: 'col-md-6'
    }
  })
);

search.addWidget(
  instantsearch.widgets.pagination({
    container: '#pagination'
  })
);

// Add this after all the search.addWidget() calls
search.start();


