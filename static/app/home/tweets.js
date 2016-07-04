import fetch from 'isomorphic-fetch';

const search = (val) => (
  fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query: val,
    }),
  })
  .then(res => res.json())
  .catch(err => console.log(err))
);

export default search;
