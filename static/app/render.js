const cb = () => {};
const render = (html, callback = cb) => {
  const app = document.getElementById('app');
  app.innerHTML = html;
  callback();
};

export default render;
