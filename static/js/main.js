// Toast Notification System
class Toast {
    static show(message, type = 'success', duration = 3000) {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type} animate-fade-in`;
        toast.textContent = message;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.classList.remove('animate-fade-in');
            toast.classList.add('animate-fade-out');
            setTimeout(() => toast.remove(), 500);
        }, duration);
    }
}

// Game State Management
class GameState {
    static async save(gameType, stateData) {
        try {
            const response = await fetch('/games/save-state', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ gameType, stateData }),
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving game state:', error);
            Toast.show('Failed to save game state', 'error');
        }
    }

    static async load(gameType) {
        try {
            const response = await fetch(`/games/load-state/${gameType}`);
            return await response.json();
        } catch (error) {
            console.error('Error loading game state:', error);
            Toast.show('Failed to load game state', 'error');
        }
    }
}

// Score Management
class ScoreManager {
    static async submitScore(gameType, score) {
        try {
            const response = await fetch('/games/submit-score', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ gameType, score }),
            });
            const data = await response.json();
            if (data.highScore) {
                Toast.show('New High Score!', 'success');
            }
            return data;
        } catch (error) {
            console.error('Error submitting score:', error);
            Toast.show('Failed to submit score', 'error');
        }
    }

    static async getLeaderboard(gameType) {
        try {
            const response = await fetch(`/games/leaderboard/${gameType}`);
            return await response.json();
        } catch (error) {
            console.error('Error loading leaderboard:', error);
            Toast.show('Failed to load leaderboard', 'error');
        }
    }
}

// Animation Utilities
const animate = {
    fadeIn: (element, duration = 500) => {
        element.style.opacity = 0;
        element.style.display = 'block';
        element.style.transition = `opacity ${duration}ms`;
        setTimeout(() => element.style.opacity = 1, 10);
    },

    fadeOut: (element, duration = 500) => {
        element.style.opacity = 1;
        element.style.transition = `opacity ${duration}ms`;
        element.style.opacity = 0;
        setTimeout(() => element.style.display = 'none', duration);
    },

    shake: (element) => {
        element.classList.add('animate-shake');
        setTimeout(() => element.classList.remove('animate-shake'), 500);
    }
};

// Sound Effects
class SoundManager {
    static sounds = {};

    static preload(soundEffects) {
        for (const [name, url] of Object.entries(soundEffects)) {
            const audio = new Audio(url);
            this.sounds[name] = audio;
        }
    }

    static play(name) {
        if (this.sounds[name]) {
            this.sounds[name].currentTime = 0;
            this.sounds[name].play();
        }
    }
}

// Event Delegation Helper
function delegate(element, eventType, selector, handler) {
    element.addEventListener(eventType, (event) => {
        const target = event.target.closest(selector);
        if (target && element.contains(target)) {
            handler.call(target, event);
        }
    });
}

// Responsive Grid Helper
function createResponsiveGrid(container, itemCount, minWidth = 100) {
    const containerWidth = container.offsetWidth;
    const columns = Math.floor(containerWidth / minWidth);
    container.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;
}

// Export utilities for use in game modules
window.GameUtils = {
    Toast,
    GameState,
    ScoreManager,
    animate,
    SoundManager,
    delegate,
    createResponsiveGrid
}; 