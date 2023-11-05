#上記2つはある程度のこす
#再帰の方法・こちらの方が行数は少ないが、再帰使用しないのも思ったよりもわかりやすいのでこちらは採用しない
def __combine_v1(lists, prefix=[]):
    if not lists:
        # もう組み合わせるリストがない場合、これまでの組み合わせを返す
        return [prefix]
    else:
        # 組み合わせるリストがまだある場合、再帰を利用して組み合わせを作る
        result = []
        for item in lists[0]:
            result.extend(combine(lists[1:], prefix + [item]))
        return result

#下記でいいはず・検証は必要
def __combine_v2(lists):
    if not lists:
        return []
    
    # スタックに最初の要素を初期状態として追加
    stack = [[item] for item in lists[0]]
    result = []
    
    while stack:
        current = stack.pop()
        # 現在の組み合わせの長さが元のリストの長さと等しい場合、結果に追加
        if len(current) == len(lists):
            result.append(current)
        else:
            # 現在の組み合わせに次の要素を追加して新しい組み合わせを作る
            next_list = lists[len(current)]
            for item in next_list:
                new_combination = current + [item]
                stack.append(new_combination)
    
    return result



class Client:
    def __init__(self):
        self.__items = {}
    
    def set_status(self, statuses):
        keys = statuses.items.keys()
        tmp_statuses = []
        for key in keys:
            self.__items[key] = []
            tmp_statuses.append(statuses.items[key])
        
        tmp_array2 = self.__combine(tmp_statuses)

        for line in tmp_array2:
            for item in line:
                self.__items[item.column_name].append(item)

    def __combine(self, lists):
        if not lists:
            return []
    
        # スタックに最初の要素を初期状態として追加
        stack = [[item] for item in lists[0]]
        result = []
        
        while stack:
            current = stack.pop()
            # 現在の組み合わせの長さが元のリストの長さと等しい場合、結果に追加
            if len(current) == len(lists):
                result.append(current)
            else:
                # 現在の組み合わせに次の要素を追加して新しい組み合わせを作る
                next_list = lists[len(current)]
                for item in next_list:
                    new_combination = current + [item]
                    stack.append(new_combination)
        
        return result