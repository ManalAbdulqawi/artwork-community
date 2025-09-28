const editBtn = document.getElementById('editBtn');
 const textarea = document.getElementById("id_description");
  const form = document.getElementById('editForm');
  const submitBtn = document.getElementById('editArtBtnSubmit');
  if (editBtn){
  editBtn.addEventListener('click', () => {
      // Get the inner text of the description div
      const description = editBtn.getAttribute('data-description');
      // Fill the textarea
      textarea.value = description;
    
    submitBtn.innerText = 'Update';
    form.setAttribute("action", "edit_artwork/");
    });}


const deleteArtModal = new bootstrap.Modal(document.getElementById("deleteArtModal"));
const deleteButton = document.getElementById("deleteBtn");
const deleteArtConfirm = document.getElementById("deleteArtConfirm");
 if (editBtn){
   deleteButton.addEventListener("click", (e) => {
   deleteArtConfirm.href = "delete_artwork/";
    deleteArtModal.show();
  });}


