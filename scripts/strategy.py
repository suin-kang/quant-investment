import pandas as pd
import matplotlib.pyplot as plt

def moving_average_strategy(data, short_window=10, long_window=50):
    """
    이동평균선 크로스오버 전략.
    """
    # 'Close' 열을 숫자로 변환
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    data.dropna(subset=['Close'], inplace=True)  # NaN 값 제거

    data['SMA_short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['Close'].rolling(window=long_window).mean()

    # 매수/매도 신호
    data['Signal'] = 0
    data.loc[data['SMA_short'] > data['SMA_long'], 'Signal'] = 1  # 매수
    data.loc[data['SMA_short'] <= data['SMA_long'], 'Signal'] = -1  # 매도

    return data

if __name__ == "__main__":
    # 데이터 로드
    data = pd.read_csv("data/O.csv", index_col="Date", parse_dates=True)
    
    # 데이터 정리
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    data.dropna(subset=['Close'], inplace=True)


    # 전략 실행
    strategy_data = moving_average_strategy(data)

    # 결과 시각화
    plt.figure(figsize=(12, 6))
    plt.plot(strategy_data.index, strategy_data['Close'], label='Close Price', alpha=0.5)
    plt.plot(strategy_data.index, strategy_data['SMA_short'], label='10-Day SMA', alpha=0.75)
    plt.plot(strategy_data.index, strategy_data['SMA_long'], label='50-Day SMA', alpha=0.75)
    plt.title("Moving Average Crossover Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()




