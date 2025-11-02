/*
  This file contains code for copying items to the
  clipboard programatically.
*/

/* Use strict mode, if supported, for the contents of this file. */
'use strict';

/*
  The following two functions are adapted from an entry from
  users Dean Taylor and Peter Mortensen on Stack Overflow at:

  https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript
*/
function fallbackCopyTextToClipboard(text)
{
  /*
    Create a text area element with the content to be copied and
    give it the focus.
  */
  var textArea = document.createElement("textarea");
  textArea.value = text;
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  /* Attempt to copy the text. */
  try
  {
    var status = document.execCommand('copy');

    if(!status)
    {
      console.error('Could not copy text using new execCommand');
    }
  }
  catch (err) {
    console.error('Could not copy text using new execCommand: ', err);
  }

  /* Get rid of the text area. */
  document.body.removeChild(textArea);

  /* Done, return. */
  return;
}


function copyTextToClipboard(text) {
  /* See if we can directly access the clipboard. */
  if(!navigator.clipboard)
  {
    fallbackCopyTextToClipboard(text);

    return;
  }

  /* Attempt to use the new API. */
  navigator.clipboard.writeText(text).then(function() {},
                                           function(err) {
    console.error('Could not copy text using new API: ', err);
  });
}

/*
  End of material adapted from Stack Overflow.
*/

/* When document is loaded, set up copy buttons. */
jQuery(document).ready(function() {
  jQuery("button.copy-prior-text").each(
    function(){set_up_copy_button(this);});});

/* Set up a single button. */
function set_up_copy_button(element)
{
  /* Find the relevant text. */
  var text = null;

  /* Attempt to get text from previous sibling. */
  for(var previous = element.previousSibling;
      previous != null;
      previous = previous.previousSibling)
  {
    /* See if the node is a text node. */
    text = previous.nodeValue;

    if(text != null)
    {
      if(text.trim() != '')
      {
        break;
      }
      else
      {
        continue;
      }
    }

    /* See if the node is an element node. */
    if(('textContent' in previous) &&
       (previous.textContent != null))
    {
      text = previous.textContent;

      break;
    }
  }

  /* See if we found text. */
  if(text != null)
  {
    /* Set the button's title. */
    element.title = "Copy " + text + " to clipboard";

    /* Listen for button clicks. */
    element.addEventListener('click', function(event) {
      copyTextToClipboard(text);});
  }
  else
  {
    console.log('Unable to set up copy button, ' + element);
  }
}
