# Cloud Storage Kubernetes Deployment

## 프로젝트 개요
이 프로젝트는 클라우드 스토리지 웹 애플리케이션을 위한 쿠버네티스 기반의 인프라 구축 및 자동화된 배포 파이프라인을 구현한 것입니다. GitOps 방식으로 운영되어 코드 변경 시 자동으로 배포가 이루어집니다.

## 주요 기능 및 특징

### 1. 고가용성 및 확장성
- **Horizontal Pod Autoscaling (HPA)**
  - CPU 사용률 30%, 메모리 사용률 70% 기준으로 자동 스케일링
  - 최소 4개, 최대 10개의 파드로 동적 확장
- **롤링 업데이트 전략**
  - 무중단 배포 구현
  - 최대 1개의 파드만 동시에 업데이트

### 2. 모니터링 및 알림 시스템
- **Prometheus & Grafana**
  - 실시간 시스템 메트릭 수집
  - 대시보드를 통한 시각화
  - NodePort를 통한 외부 접근 (Prometheus: 30090, Grafana: 30030)
- **AlertManager**
  - Slack을 통한 실시간 알림
  - CPU 사용량, 파드 상태 등 주요 지표 모니터링
  - 심각도별 알림 분류 (warning, critical, info)

### 3. 스토리지 관리
- **Persistent Volume (PV) & PVC**
  - 100GB NFS 기반 스토리지
  - ReadWriteMany 접근 모드로 다중 파드 접근 지원
  - 데이터 영속성 보장

### 4. 네트워크 구성
- **MetalLB**
  - 로드밸런서 구현
  - IP 풀 관리 (192.168.1.17-192.168.1.35)
- **Service**
  - NodePort 타입으로 외부 접근 제공
  - 웹 서비스 (30088), 메트릭스 (30092) 포트 노출

### 5. 부하 테스트
- **Locust**
  - 자동화된 부하 테스트 스크립트
  - 로그인 및 기본 기능 테스트 구현

## 기술 스택
- Kubernetes
- Prometheus Stack (Prometheus, Grafana, AlertManager)
- MetalLB
- NFS
- GitOps (ArgoCD)

## 아키텍처
```
[외부 요청] → [MetalLB] → [Kubernetes Service] → [Pod]
                    ↓
[Prometheus] ← [ServiceMonitor] ← [Pod Metrics]
                    ↓
[AlertManager] → [Slack 알림]
```

## 모니터링 지표
- CPU 사용률
- 메모리 사용률
- 파드 상태
- 서비스 가용성
- 네트워크 트래픽

## 자동화된 알림 조건
- CPU 사용률 50% 초과 (1분 이상)
- 파드 다운 상태 (1분 이상)
- 새로운 파드 생성 감지 