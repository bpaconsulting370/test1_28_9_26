/* Business Process Automation — small progressive enhancements.
   Nothing on the site depends on this file: if it fails to load, every page still works. */
(function () {
  'use strict';

  /* 1. Contact form: if the visitor arrived via an "Enquire about this" button,
        mention what they were looking at (the button adds ?service=Name to the link). */
  var topic = new URLSearchParams(window.location.search).get('service');
  var message = document.getElementById('c-message');
  if (topic && message && !message.value) {
    message.value = "I'm interested in: " + topic.slice(0, 120) + '\n\n';
  }

  /* 2. Retro hit counter: shows this page's REAL view count from GoatCounter.
        It stays hidden unless the count loads, so visitors never see a made-up number.
        Needs "Allow adding visitor counts on your website" switched on in GoatCounter settings. */
  var box = document.getElementById('visitcount');
  var code = box && box.getAttribute('data-gc');
  if (box && code && code !== 'YOUR-CODE' && window.fetch) {
    fetch('https://' + code + '.goatcounter.com/counter/' + window.location.pathname + '.json')
      .then(function (r) { return r.ok ? r.json() : Promise.reject(new Error('counter unavailable')); })
      .then(function (data) {
        var n = String((data && data.count) || '').replace(/[^0-9]/g, '');
        if (!n) { return; }
        document.getElementById('hit-counter').textContent = ('000000' + n).slice(-Math.max(6, n.length));
        box.hidden = false;
      })
      .catch(function () { /* leave the counter hidden */ });
  }

  /* 3. Forms: until formspree_id is set in _config.yml, tell the site owner instead of
        sending visitors to a broken endpoint. */
  var forms = document.querySelectorAll('form[action*="YOUR-FORM-ID"]');
  Array.prototype.forEach.call(forms, function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      window.alert('This form is not connected yet. The site owner needs to set formspree_id in _config.yml.');
    });
  });
})();
