import { ChatEngine } from 'react-chat-engine';

import ChatFeed from './components/ChatFeed';

import './App.css';

const App = () => {
    return (
        <ChatEngine
            height = "100vh"
            projectID="32073c06-7df5-4705-8480-120475a4ab15"
            userName="jsm"
            userSecret="123123"
            renderChatFeed= {(chatAppProps) => <ChatFeed {... chatAppProps} />
            }
        />
    )
}

export default App;