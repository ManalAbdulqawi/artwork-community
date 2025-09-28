


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





const editButtons = document.getElementsByClassName("commentEdit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
    console.log("manaaal")
  button.addEventListener("click", (e) => {
    console.log("saleh")
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("commentDelete");
const deleteConfirm = document.getElementById("deleteConfirm");
/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}






