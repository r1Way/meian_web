// 从localStorage读取评论
function loadComments() {
    const comments = JSON.parse(localStorage.getItem('comments')) || [];
    const commentsDiv = document.getElementById('comments');
    commentsDiv.innerHTML = '';
    comments.forEach((comment, index) => {
      const commentDiv = document.createElement('div');
      commentDiv.className = 'comment';
      commentDiv.innerHTML = `
        <p style="display: inline;">${comment.text}</p>
        <a href="#" class="delete-button" onclick="deleteComment(${index})">删除按钮</a>
      `;
      commentsDiv.appendChild(commentDiv);
    });
  }

  // 添加评论到localStorage
  function addComment() {
    const input = document.getElementById('commentInput');
    const text = input.value.trim();
    if (text) {
      const comments = JSON.parse(localStorage.getItem('comments')) || [];
      comments.push({ text });
      localStorage.setItem('comments', JSON.stringify(comments));
      loadComments(); // 重新加载评论以显示新添加的评论
      input.value = ''; // 清空输入框
    }
  }

  // 删除评论并更新localStorage
  function deleteComment(index) {
    const comments = JSON.parse(localStorage.getItem('comments')) || [];
    comments.splice(index, 1);
    localStorage.setItem('comments', JSON.stringify(comments));
    loadComments(); // 重新加载评论以显示删除后的评论列表
  }

  // 切换显示区域
  function toggleSection(sectionId) {
    const commentsSection = document.getElementById('commentSection');
    const qaSection = document.getElementById('qaSection');
    const commentBtn=document.getElementById('comment-button');
    const qaBtn=document.getElementById('qa-button');
    commentBtn.classList.remove('active');
    qaBtn.classList.remove('active');
    commentsSection.classList.remove('active');
    qaSection.classList.remove('active');
    console.log(sectionId);
    if (sectionId === 'comment') {
          commentsSection.classList.toggle('active');
          commentBtn.classList.toggle('active');
          loadComments();
      } else if (sectionId === 'qa') {
          qaSection.classList.toggle('active');
          qaBtn.classList.toggle('active');
      }
  }

  // 页面加载时加载评论
  window.onload = loadComments;