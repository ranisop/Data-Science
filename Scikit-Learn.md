# Data-Science

## 🌸 모형 최적화
- 머신러닝 모형이 완성된 후에는 최적화 과정을 통해 예측 성능을 향상시킨다.
<br>

### Scikit-Learn의 모형 하이퍼 파라미터 튜닝 구조
- Scikit-Learn에서는 다음과 같은 모형 최적화 도구를 지원한다.
> - validation_curve  
단일 하이퍼 파라미터 최적화
> - GridSearchCV  
그리드를 사용한 복수 하이퍼 파라미터 최적화
> - ParameterGrid  
복수 파라미터 최적화용 그리드


```
1. validation_curve
```
- `validation_curve` 함수는 최적화할 파라미터 이름과 범위, 그리고 성능 기준을 `param_name`, `param_range`, `scoring` 인수로 받아 파라미터 범위의 모든 경우에 대해 성능 기준을 계산한다.


```
2. GridSearchCV
```
- `GridSearchCV` 클래스는 `validation_curve` 함수와 달리 모형 래퍼(Wrapper) 성격의 클래스이다. 클래스 객체에 `fit` 메서드를 호출하면 grid search를 사용하여 자동으로 복수개의 내부 모형을 생성하고 이를 모두 실행시켜서 최적 파라미터를 찾아준다. 생성된 복수개와 내부 모형과 실행 결과는 다음 속성에 저장된다.
> - `grid_scores_`  
>   - param_grid의 모든 파라미터 조합에 대한 성능 결과. 각각의 원소는 다음 요소로 이루어진 튜플이다.
>   - parameters: 사용된 파라미터
>   - mean_validation_score: 교차 검증(cross-validation) 결과의 평균값
>   - cv_validation_scores: 모든 교차 검증(cross-validation) 결과
> - `best_score_`
>   - 최고 점수
> - `best_params_`
>   - 최고 점수를 낸 파라미터
> - `best_estimator_`
>   - 최고 점수를 낸 파라미터를 가진 모형


```
3. ParameterGrid
```
- 때로는 scikit-learn이 제공하는 GridSearchCV 이외의 방법으로 그리드 탐색을 해야하는 경우도 있다. 이 경우 파라미터를 조합하여 탐색 그리드를 생성해 주는 명령어가 `ParameterGrid`이다. `ParameterGrid`는 탐색을 위한 iterator 역할을 한다.
<br>

### 병렬 처리
- `GridSearchCV` 명령에는 `n_jobs`라는 인수가 있다. 디폴트 값은 1인데 이 값을 증가시키면 내부적으로 멀티 프로세스를 사용하여 그리드서치를 수행한다. 만약 CPU 코어의 수가 충분하다면 `n_jobs`를 늘릴수록 속도가 증가한다.

<br>
<br>


* 출처: [데이터 사이언스 스쿨](https://datascienceschool.net/view-notebook/ff4b5d491cc34f94aea04baca86fbef8/)









