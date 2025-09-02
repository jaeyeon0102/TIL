class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt  # 상품 개수
        self.IDs = IDs  # [int] * 5 # 상품 ID 리스트
products = {}
count_by_cc = [[0] * 6 for _ in range(6)]
def init() -> None:
    global products, count_by_cc
    products.clear # 변수 초기화
    count_by_cc = [[0] * 6 for _ in range(6)]

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    # true는 판매중이라는 뜻
    products[mID] = (mCategory, mCompany, mPrice, True)

    count_by_cc[mCategory][mCompany] += 1
    return count_by_cc[mCategory][mCompany]

def closeSale(mID : int) -> int:
    if mID not in products:
        return -1
    cat, com, price, on_sale = products[mID]

    if not on_sale:
        return -1
    
    products[mID] = (cat,com, price, False)
    count_by_cc[cat][com] -= 1

    return price

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    for mID in products:
        cat, com, price, on_sale = products[mID]

        if cat == mCategory and com == mCompany and on_sale:
            new_price = price - mAmount
            if new_price <= 0:
                products[mID] = (cat, com, price, False)
                count_by_cc[cat][com] -= 1

            else:
                products[mID] = (cat,com, new_price, True)

    return count_by_cc[mCategory][mCompany]

def show(mHow : int, mCode : int) -> RESULT:
    candidates = []

    for mID, (cat,com,price,on_sale) in products.items():
        if not on_sale:
            continue

        if mHow == 0:
            pass
        elif mHow == 1 and cat != mCode:
            continue
        elif mHow == 2 and com != mCode:
            continue


        candidates.append((price,mID))

    candidates.sort()

    top5 = candidates[:5]
    cnt = len(top5)

    IDs = [mID for _, mID in top5] + [0] * (5-cnt)
    return RESULT(cnt, IDs)