const TheirMessage = ({ lastMessage, message}) => {
    const isFirstMessageByUser = !lastMessage || lastMessage.sender.username !== message.sender.username;

    return (
        <div class="message-row">
            TheirMessage
        </div>
    )
}

export default TheirMessage