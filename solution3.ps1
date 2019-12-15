$text = "this is sri nandan patel"

##number of characters

$char_len = $text.length
write-output "Total character length:$char_len"

##number of words

$num_word = ($text.split()).count
write-output "Total word count:$num_word"

##Number of alphabets

$num_aplha = ($text | measure-object -character -ignorewhitespace).characters
write-output "Total alphabets:$num_alpha"

##common occuring alphabets

$com_ocr_alpha = $text_joint.GetEnumerator() | group -NoElement | sort count