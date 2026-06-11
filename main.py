# [4. 2차원 리스트 설계] 가상 식품 영양 성분 데이터 (100g 기준)
food_data = [
    ["닭가슴살", 120, 0, 23, 1],
    ["고구마", 130, 32, 1, 0],
    ["현미밥", 150, 33, 3, 1],
    ["계란후라이", 140, 1, 12, 10]
]

# [5. 함수 설계 - 1] 메뉴 및 안내 출력
def show_menu():
    print("\n" + "="*40)
    print("      ★ 개인 맞춤형 영양 계산기 ★      ")
    print("="*40)
    print(" 현재 등록된 음식: 닭가슴살, 고구마, 현미밥, 계란후라이")
    print(" 수시로 음식을 입력하고, '종료'를 입력하면 정산됩니다.")
    print("="*40)

# [5. 함수 설계 - 2] 영양소 계산 함수
def calculate_nutrition(food_name, weight):
    # [6. 제어구조 - 반복문 1] 2차원 리스트 탐색
    for food in food_data:
        # [6. 제어구조 - 조건문 1] 음식 이름 매칭
        if food[0] == food_name:
            # 100g 기준 데이터이므로 섭취량(weight) 비율을 곱해줌
            ratio = weight / 100
            cal = food[1] * ratio
            carbs = food[2] * ratio
            protein = food[3] * ratio
            fat = food[4] * ratio
            return [cal, carbs, protein, fat]
            
    # [7. 예외 상황 1] 음식을 찾지 못했을 때
    return None

# [5. 함수 설계 - 3] 최종 보고서 출력 함수
def print_report(total_nutrients, goal_calories):
    total_cal = total_nutrients[0]
    total_carbs = total_nutrients[1]
    total_protein = total_nutrients[2]
    total_fat = total_nutrients[3]
    
    # 달성률 계산
    achievement_rate = (total_cal / goal_calories) * 100
    
    print("\n" + "="*15 + " 오늘의 영양 리포트 " + "="*15)
    print(f"▶ 총 섭취 칼로리: {total_cal:.1f} kcal / 목표: {goal_calories} kcal")
    print(f"▶ 탄수화물: {total_carbs:.1f}g | 단백질: {total_protein:.1f}g | 지방: {total_fat:.1f}g")
    print(f"▶ 칼로리 달성률: {achievement_rate:.1f}%")
    print("-"*43)
    
    # [6. 제어구조 - 조건문 3] 최종 영양 충족도 등급 판정
    if achievement_rate < 80:
        print("결과: [에너지 부족] 조금 더 균형 잡힌 식사로 칼로리를 채워보세요!")
    elif achievement_rate <= 120:
        print("결과: [적정 식사] 아주 훌륭합니다! 목표량에 맞게 잘 드셨습니다.")
    else:
        print("결과: [에너지 과잉 경고] 목표 칼로리를 초과했습니다. 활동량을 늘려보세요!")
    print("="*43)

# ==========================================
# 메인 프로그램 로직 [6. 제어구조 - 반복문 2 (while문)]
# ==========================================
def main():
    show_menu()
    
    # [6. 제어구조 - 조건문 2 / 7. 예외 상황 2] 목표 칼로리 예외 처리
    while True:
        try:
            goal_calories = int(input("하루 목표 칼로리를 입력하세요 (kcal): "))
            if goal_calories <= 0:
                print("⚠️ 오류: 목표 칼로리는 0보다 커야 합니다. 다시 입력해주세요.")
                continue
            break
        except ValueError:
            print("⚠️ 오류: 숫자만 입력 가능합니다.")

    # 누적할 영양소 데이터 [총 칼로리, 총 탄수화물, 총 단백질, 총 지방]
    total_nutrients = [0.0, 0.0, 0.0, 0.0]
    
    while True:
        print("\n" + "-"*40)
        food_name = input("먹은 음식을 입력하세요 (종료하려면 '종료' 입력): ").strip()
        
        if food_name == "종료":
            break
            
        # [7. 예외 상황 1] 음식 검색 및 예외 처리
        result = calculate_nutrition(food_name, 100) # 먼저 등록 여부 확인용
        if result is None:
            print("⚠️ 해당 음식을 찾을 수 없습니다. 다시 입력해 주세요.")
            continue
            
        # [6. 제어구조 - 조건문 2 / 7. 예외 상황 2] 섭취량 예외 처리
        while True:
            try:
                weight = int(input(f"'{food_name}'의 섭취량을 입력하세요 (g): "))
                if weight <= 0:
                    print("⚠️ 오류: 섭취량은 0보다 커야 합니다. 다시 입력해주세요.")
                    continue
                break
            except ValueError:
                print("⚠️ 오류: 숫자만 입력 가능합니다.")
        
        # 실제 섭취량 기반 재계산 및 누적
        real_result = calculate_nutrition(food_name, weight)
        for i in range(4):
            total_nutrients[i] += real_result[i]
            
        print(f"✓ {food_name} {weight}g 추가 완료! (현재 누적: {total_nutrients[0]:.1f} kcal)")

    # [3. 출력] 최종 결과 리포트 출력
    print_report(total_nutrients, goal_calories)

# 프로그램 실행
if __name__ == "__main__":
    main()
