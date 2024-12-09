import yfinance as yf
import pandas as pd
import os

def fetch_data(symbol, start_date, end_date, save_dir="data"):
    """
    금융 데이터를 Yahoo Finance에서 가져옵니다.
    """
    os.makedirs(save_dir, exist_ok=True)  # 데이터 디렉토리 생성
    data = yf.download(symbol, start=start_date, end=end_date)

    # 인덱스를 "Date"로 변경
    data.reset_index(inplace=True)

    # 파일 저장
    file_path = f"{save_dir}/{symbol}.csv"
    data.to_csv(file_path, index=False)
    print(f"{symbol} 데이터가 {file_path}에 저장되었습니다.")
    return data


if __name__ == "__main__":
    # 리얼티 인컴 데이터 수집
    fetch_data("O", "2010-01-01", "2023-12-31")

